# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 417
- HTTP: 92 alive / 61 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36135
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
