# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 420
- HTTP: 106 alive / 73 gold
- HTTPS: 42 alive / 25 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49458
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
