# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 417
- HTTP: 104 alive / 71 gold
- HTTPS: 137 alive / 18 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41289
- Ever gold: 1321

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
