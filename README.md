# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 411
- HTTP: 116 alive / 62 gold
- HTTPS: 157 alive / 17 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41006
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
