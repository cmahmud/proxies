# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 462
- HTTP: 152 alive / 91 gold
- HTTPS: 127 alive / 36 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46871
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
