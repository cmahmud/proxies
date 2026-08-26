# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 395
- HTTP: 178 alive / 69 gold
- HTTPS: 104 alive / 21 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 203 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39487
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
