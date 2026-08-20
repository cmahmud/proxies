# SyndProxy private pool

## Current pool

- Alive now: 633
- Gold now: 385
- HTTP: 158 alive / 62 gold
- HTTPS: 73 alive / 15 gold
- SOCKS4: 199 alive / 153 gold
- SOCKS5: 203 alive / 155 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25720
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
