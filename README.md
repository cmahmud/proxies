# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 392
- HTTP: 110 alive / 57 gold
- HTTPS: 56 alive / 13 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33529
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
