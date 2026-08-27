# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 415
- HTTP: 113 alive / 69 gold
- HTTPS: 172 alive / 18 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40975
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
