# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 547
- HTTP: 445 alive / 164 gold
- HTTPS: 289 alive / 106 gold
- SOCKS4: 209 alive / 133 gold
- SOCKS5: 204 alive / 144 gold

## Historical pool

- Discovered: 127345
- Ever alive: 19829
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
