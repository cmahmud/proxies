# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 416
- HTTP: 93 alive / 74 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 175 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41761
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
