# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 464
- HTTP: 150 alive / 93 gold
- HTTPS: 131 alive / 36 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46895
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
