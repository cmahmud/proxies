# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 391
- HTTP: 244 alive / 77 gold
- HTTPS: 154 alive / 18 gold
- SOCKS4: 204 alive / 148 gold
- SOCKS5: 242 alive / 148 gold

## Historical pool

- Discovered: 156840
- Ever alive: 29641
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
