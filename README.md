# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 399
- HTTP: 86 alive / 55 gold
- HTTPS: 48 alive / 16 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42834
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
