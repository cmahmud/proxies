# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 262
- HTTP: 244 alive / 30 gold
- HTTPS: 166 alive / 5 gold
- SOCKS4: 217 alive / 118 gold
- SOCKS5: 216 alive / 109 gold

## Historical pool

- Discovered: 99107
- Ever alive: 11821
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
