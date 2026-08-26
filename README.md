# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 386
- HTTP: 135 alive / 73 gold
- HTTPS: 180 alive / 19 gold
- SOCKS4: 164 alive / 145 gold
- SOCKS5: 171 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39920
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
