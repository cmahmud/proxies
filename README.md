# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 400
- HTTP: 91 alive / 58 gold
- HTTPS: 167 alive / 15 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41028
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
