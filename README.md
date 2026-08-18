# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 242
- HTTP: 280 alive / 34 gold
- HTTPS: 181 alive / 8 gold
- SOCKS4: 265 alive / 134 gold
- SOCKS5: 205 alive / 66 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
