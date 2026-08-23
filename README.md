# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 220
- HTTP: 173 alive / 56 gold
- HTTPS: 109 alive / 11 gold
- SOCKS4: 90 alive / 70 gold
- SOCKS5: 142 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32684
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
