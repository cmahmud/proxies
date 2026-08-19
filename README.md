# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 533
- HTTP: 413 alive / 158 gold
- HTTPS: 283 alive / 87 gold
- SOCKS4: 234 alive / 157 gold
- SOCKS5: 202 alive / 131 gold

## Historical pool

- Discovered: 119819
- Ever alive: 18185
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
