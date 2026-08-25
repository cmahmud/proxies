# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 416
- HTTP: 109 alive / 63 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36070
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
