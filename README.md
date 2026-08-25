# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 418
- HTTP: 81 alive / 60 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36183
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
