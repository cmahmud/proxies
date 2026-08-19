# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 523
- HTTP: 400 alive / 152 gold
- HTTPS: 253 alive / 83 gold
- SOCKS4: 241 alive / 152 gold
- SOCKS5: 205 alive / 136 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17987
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
