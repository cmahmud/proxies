# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 411
- HTTP: 90 alive / 58 gold
- HTTPS: 64 alive / 19 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36210
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
