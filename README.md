# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 403
- HTTP: 87 alive / 59 gold
- HTTPS: 65 alive / 16 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42738
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
