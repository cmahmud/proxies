# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 427
- HTTP: 94 alive / 66 gold
- HTTPS: 90 alive / 27 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35704
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
