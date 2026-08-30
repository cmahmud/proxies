# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 440
- HTTP: 105 alive / 82 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44567
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
