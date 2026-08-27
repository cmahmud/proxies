# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 400
- HTTP: 95 alive / 61 gold
- HTTPS: 181 alive / 14 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40648
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
