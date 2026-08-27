# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 411
- HTTP: 110 alive / 63 gold
- HTTPS: 137 alive / 19 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41371
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
