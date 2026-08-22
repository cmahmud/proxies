# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 424
- HTTP: 340 alive / 88 gold
- HTTPS: 217 alive / 31 gold
- SOCKS4: 252 alive / 147 gold
- SOCKS5: 272 alive / 158 gold

## Historical pool

- Discovered: 164928
- Ever alive: 32168
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
