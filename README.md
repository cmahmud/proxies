# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 384
- HTTP: 165 alive / 64 gold
- HTTPS: 83 alive / 16 gold
- SOCKS4: 196 alive / 151 gold
- SOCKS5: 203 alive / 153 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25726
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
