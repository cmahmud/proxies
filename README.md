# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 465
- HTTP: 136 alive / 94 gold
- HTTPS: 113 alive / 35 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 209 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46399
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
