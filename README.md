# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 400
- HTTP: 135 alive / 67 gold
- HTTPS: 157 alive / 14 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 196 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40533
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
