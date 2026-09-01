# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 421
- HTTP: 93 alive / 66 gold
- HTTPS: 61 alive / 24 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47073
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
