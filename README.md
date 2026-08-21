# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 386
- HTTP: 272 alive / 74 gold
- HTTPS: 163 alive / 18 gold
- SOCKS4: 220 alive / 149 gold
- SOCKS5: 238 alive / 145 gold

## Historical pool

- Discovered: 156831
- Ever alive: 29631
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
