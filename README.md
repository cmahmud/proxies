# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 340
- HTTP: 115 alive / 40 gold
- HTTPS: 69 alive / 10 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 182 alive / 139 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32819
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
