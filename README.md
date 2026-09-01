# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 463
- HTTP: 149 alive / 93 gold
- HTTPS: 121 alive / 35 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46871
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
