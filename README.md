# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 402
- HTTP: 85 alive / 58 gold
- HTTPS: 48 alive / 16 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42834
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
