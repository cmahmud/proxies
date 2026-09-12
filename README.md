# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 424
- HTTP: 109 alive / 80 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49470
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
