# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 368
- HTTP: 299 alive / 77 gold
- HTTPS: 211 alive / 25 gold
- SOCKS4: 220 alive / 125 gold
- SOCKS5: 231 alive / 141 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32323
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
