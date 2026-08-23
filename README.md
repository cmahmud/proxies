# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 200
- HTTP: 158 alive / 35 gold
- HTTPS: 53 alive / 6 gold
- SOCKS4: 224 alive / 68 gold
- SOCKS5: 242 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32780
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
