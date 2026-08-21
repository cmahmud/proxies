# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 420
- HTTP: 212 alive / 83 gold
- HTTPS: 144 alive / 26 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 267 alive / 169 gold

## Historical pool

- Discovered: 155792
- Ever alive: 29337
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
