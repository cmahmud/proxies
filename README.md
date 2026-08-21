# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 353
- HTTP: 230 alive / 77 gold
- HTTPS: 192 alive / 22 gold
- SOCKS4: 200 alive / 124 gold
- SOCKS5: 187 alive / 130 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29801
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
