# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 410
- HTTP: 223 alive / 76 gold
- HTTPS: 157 alive / 24 gold
- SOCKS4: 229 alive / 150 gold
- SOCKS5: 227 alive / 160 gold

## Historical pool

- Discovered: 151066
- Ever alive: 27386
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
