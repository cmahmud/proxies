# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 417
- HTTP: 256 alive / 84 gold
- HTTPS: 198 alive / 19 gold
- SOCKS4: 225 alive / 161 gold
- SOCKS5: 234 alive / 153 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30032
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
