# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 201
- HTTP: 174 alive / 44 gold
- HTTPS: 191 alive / 9 gold
- SOCKS4: 111 alive / 65 gold
- SOCKS5: 170 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32680
- Ever gold: 1196

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
