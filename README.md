# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 242
- HTTP: 233 alive / 31 gold
- HTTPS: 112 alive / 8 gold
- SOCKS4: 235 alive / 115 gold
- SOCKS5: 198 alive / 88 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6880
- Ever gold: 323

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
