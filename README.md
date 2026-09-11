# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 440
- HTTP: 102 alive / 79 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49177
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
