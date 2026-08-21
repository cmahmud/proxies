# SyndProxy private pool

## Current pool

- Alive now: 1171
- Gold now: 435
- HTTP: 415 alive / 110 gold
- HTTPS: 282 alive / 26 gold
- SOCKS4: 233 alive / 154 gold
- SOCKS5: 241 alive / 145 gold

## Historical pool

- Discovered: 160024
- Ever alive: 30561
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
