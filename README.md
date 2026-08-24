# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 398
- HTTP: 158 alive / 64 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 193 alive / 159 gold
- SOCKS5: 209 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33336
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
