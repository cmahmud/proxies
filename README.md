# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 423
- HTTP: 106 alive / 71 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48971
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
