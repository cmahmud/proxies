# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 417
- HTTP: 108 alive / 63 gold
- HTTPS: 84 alive / 18 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36070
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
