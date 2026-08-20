# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 402
- HTTP: 197 alive / 85 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 192 alive / 144 gold
- SOCKS5: 248 alive / 151 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27427
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
