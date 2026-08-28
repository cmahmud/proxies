# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 404
- HTTP: 93 alive / 63 gold
- HTTPS: 108 alive / 13 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43031
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
